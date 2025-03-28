from django.shortcuts import render
from .models import Post

def post_search(request):
    query = request.GET.get('q', '')  # Get search query from URL parameter 'q'
    
    # Filter posts based on the query, matching title, tags, or content
    posts = Post.objects.filter(
        title__icontains=query  # Search by title (case-insensitive)
    )
    
    # If a query is present, also filter by tags and content
    if query:
        posts = posts.filter(
            title__icontains=query | 
            tags__name__icontains=query |  # Search by tags (case-insensitive)
            content__icontains=query  # Search by content (case-insensitive)
        )
    
    return render(request, 'post_search_results.html', {'posts': posts, 'query': query})
