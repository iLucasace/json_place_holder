from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'jsonplaceholder_app/post_list.html', {'posts': posts})

import plotly.graph_objs as go
from django.shortcuts import render
from .models import Post

def post_chart(request):
    # Retrieve data from the database
    posts = Post.objects.all()

    # Extract user IDs and count the number of posts for each user
    user_ids = [post.userId for post in posts]
    post_counts = {user_id: user_ids.count(user_id) for user_id in user_ids}

    # Create a bar chart using Plotly
    fig = go.Figure()

    # Add a bar trace to the chart
    fig.add_trace(
        go.Bar(
            x=list(post_counts.keys()),  # User IDs
            y=list(post_counts.values()),  # Number of posts
            marker_color='rgb(26, 118, 255)',  # Bar color
            text=list(post_counts.values()),  # Display post count as text on bars
            textposition='auto',  # Position of the text on bars
            hoverinfo='x+y',  # Display both user ID and post count in hover info
        )
    )

    # Customize chart layout
    fig.update_layout(
        title='Number of Posts by User',
        xaxis_title='User ID',
        yaxis_title='Number of Posts',
        xaxis=dict(type='category'),  # Use a categorical x-axis
        bargap=0.1,  # Gap between bars
        showlegend=False,  # Hide legend
        paper_bgcolor='rgb(243, 243, 243)',  # Background color
        plot_bgcolor='rgb(243, 243, 243)',  # Plot area color
    )

    # Convert the chart to HTML
    chart_div = fig.to_html(full_html=False)

    return render(request, 'jsonplaceholder_app/post_chart.html', {'chart_div': chart_div})

