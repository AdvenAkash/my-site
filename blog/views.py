from django.shortcuts import render
from datetime import date

all_posts =[
    {
        "slug":"hike-in-the-moutains",
        "image":"mountains.jpg",
        "author":"Akash",
        "date": date(2021,12,19),
        "title":"Mountain Hiking",
        "excerpt":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus istesaepe repellendus similique, enim vitae expedita sunt veritatis minusblanditiis",
         "content":"""Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Necessitatibus similique earum iusto tempora animi sed modi alias eum officia reiciendis ducimus voluptatum excepturi perferendis, 
        sunt eligendi dolorum molestiae, eveniet perspiciatis facere doloremque. Sequi cupiditate suscipit, molestias inventore excepturi, 
        aspernatur deserunt aliquam perspiciatis vel enim porro tenetur laborum ad voluptatum in.
        """
    },
    {
        "slug":"coding-is-fun",
        "image":"coding.jpg",
        "author":"Akash",
        "date": date(2024,9,21),
        "title":"Coding time",
        "excerpt":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus istesaepe repellendus similique, enim vitae expedita sunt veritatis minusblanditiis",
        "content":"""Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Necessitatibus similique earum iusto tempora animi sed modi alias eum officia reiciendis ducimus voluptatum excepturi perferendis, 
        sunt eligendi dolorum molestiae, eveniet perspiciatis facere doloremque. Sequi cupiditate suscipit, molestias inventore excepturi, 
        aspernatur deserunt aliquam perspiciatis vel enim porro tenetur laborum ad voluptatum in.
        """
    },
    {
        "slug":"in-the-woods",
        "image":"woods.jpg",
        "author":"Akash",
        "date": date(2022,1,23),
        "title":"Walking in the woods",
        "excerpt":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus istesaepe repellendus similique, enim vitae expedita sunt veritatis minusblanditiis",
        "content":"""Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Necessitatibus similique earum iusto tempora animi sed modi alias eum officia reiciendis ducimus voluptatum excepturi perferendis, 
        sunt eligendi dolorum molestiae, eveniet perspiciatis facere doloremque. Sequi cupiditate suscipit, molestias inventore excepturi, 
        aspernatur deserunt aliquam perspiciatis vel enim porro tenetur laborum ad voluptatum in.
        """
    }
]
def get_date(post):
    return post['date']
# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts,

    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts,
    })

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html",{
        "post":identified_post
    })