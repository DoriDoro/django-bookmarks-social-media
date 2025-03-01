# Bookmarks - Django Project  

## Description  
**Bookmarks** is a feature-rich social web application built with Django, enabling users to share images, follow 
others, and engage with content. The project implements essential user account functionalities, including 
authentication, profile management, and social interactions. Users can register, log in, and customize their profiles 
while leveraging an interactive platform to like, follow, and explore shared images.  

## Features  

### User Authentication & Management  
- Full user registration, login, and profile editing  
- Integrated Django authentication framework  
- Custom templates for login, logout, password reset, and change views  
- Extended user model with custom profile fields  
- Social authentication via Google using **Python Social Auth**  

### Social Features & Image Sharing  
- Follow/unfollow functionality to connect with other users  
- Like/unlike system for shared images  
- Activity stream to track user interactions in real time  
- Image view tracking and ranking system powered by **Redis**  

### Advanced Backend & Performance Optimizations  
- Custom authentication backend to prevent duplicate email registrations  
- Many-to-many relationships with intermediate models for flexibility  
- Optimized QuerySets for efficient database access  
- Signals for denormalizing counts and improving performance  
- Debugging with **Django Debug Toolbar**  

### Dynamic Frontend & User Experience  
- JavaScript-powered interactive features  
- Infinite scroll pagination for seamless content browsing  
- JavaScript bookmarklet to quickly save images  
- Asynchronous HTTP requests with Django & JavaScript  
- Image thumbnail generation with **easy-thumbnails**  

### Security & Deployment Enhancements  
- Enforced HTTPS for secure connections using Django Extensions  
- Media file upload configuration for handling user-generated content  

With **Bookmarks**, users can discover, share, and engage with images effortlessly, creating an interactive and social experience powered by Django! 
