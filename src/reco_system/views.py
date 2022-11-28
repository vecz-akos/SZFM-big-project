from django.shortcuts import render
from api.models import Category, Sample, Rate
from api.serializers import SampleSerializer
from django.db.models import Case, When
import random
import pandas as pd

def get_similar(sample_name,rating,corrMatrix):
    similar_ratings = corrMatrix[sample_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    
    return similar_ratings


def recommend(request):

    sample_rating = pd.DataFrame(list(Rate.objects.all().values()))

    new_user = sample_rating.user_id.unique().shape[0]
    current_user_id = request.user.id

    if current_user_id > new_user:
        sample = Sample.objects.get(id)
        q = Rate(user=request.user, sample=sample, rating=0)
        q.save()


    userRatings = sample_rating.pivot_table(index=['user_id'],columns=['sample_id'],values='rating')
    userRatings = userRatings.fillna(0,axis=1)
    corrMatrix = userRatings.corr(method='pearson')

    user = pd.DataFrame(list(Rate.objects.filter(user=request.user).values())).drop(['user_id','id'],axis=1)
    user_filtered = [tuple(x) for x in user.values]
    sample_id_watched = [each[0] for each in user_filtered]

    similar_sample = pd.DataFrame()
    for sample,rating in user_filtered:
        similar_sample = similar_sample.append(get_similar(sample,rating,corrMatrix),ignore_index = True)

    samples_id = list(similar_sample.sum().sort_values(ascending=False).index)
    samples_id_recommend = [each for each in samples_id if each not in sample_id_watched]
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(samples_id_recommend)])
    sample_list=list(Sample.objects.filter(id__in = samples_id_recommend).order_by(preserved)[:10])

    context = {'sample_list': sample_list}
    return render(request, 'rate/rate.html', context)

def get_random_sample(category="", pc=1):
    if (not category) or (not isinstance(category, int)):
        category = random.choice(Category.objects.all()).id
    samples = list(Sample.objects.filter(categoryId=category))
    if len(samples) > pc:
        samples = random.sample(samples)
    return samples
