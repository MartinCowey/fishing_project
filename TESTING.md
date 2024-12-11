# Contents


- [Validation](#validation)
  - [HTML](#html-validation)
  - [CSS](#css-validation)
  - [Javascript](#javascript-validation)
  - [Python](#python-validation)
   

- [Models](#models-)
  - [Database Schema](#database-schema)
  - [All Auth](#allauth-user-model)
  - [Blog](#blog-model)
  - [Comments](#comment-model)
  - [Custom](#custom-model)
    - [Profile custom 1](#profile-model---custom-1)
    - [Location custom 2](#location-model---custom-2)


## Validation

During the process it was important use clean code that met the relevant standards for inclusivity and responsive design. I tried to impliment accessible and compliance through out

### HTML Validation

HTML files were put through [HTML W3C Validator](https://validator.w3.org) for validation.

As we used Django and certain syntax such as '{% extends "base.html" %} we had to use the source code from the page to work with the validator:

> Right click and view the page source.
> Copy code and paste into the validate by input option.
> Address errors and warnings, fix and repeat fro each page.

All pages received the same message from the validator:
![html validation](documentation/testing/37_html.webp) 

All HTML pages were validated *see below*:

| HTML source Code/Page | Errors | Warnings |
| ---- | ----- | ------|
| Home | 0 | 0 | 0 | 
| Base | 0 | 0 | 0 | 
| Toast | 0 | 0 | 0 |
| blog_form | 0 | 0 | 0 |
| blog_post | 0 | 0 | 0 |
| blog_list | 0 | 0 | 0 |
| blog_edit | 0 | 0 | 0 |
| blog_delete | 0 | 0 | 0 |
| blog_search | 0 | 0 | 0 |
| profile_form | 0 | 0 | 0 |
| profile_detail | 0 | 0 | 0 |
| profile_confirm_delete | 0 | 0 | 0 |
| signin | 0 | 0 | 0 |
| signout | 0 | 0 | 0 |
| signup | 0 | 0 | 0 |

<hr>

### CSS Validation

CSS validation using jigsaw.w3 [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) CSS validator with no errors:

![No Errors](documentation/testing/02_css_validation.png)

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

External CSS for Bootstrap, provided by [CDN](https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css) was not tested. 


<hr>

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the 2 JavaScript files required for cooments and the terms and condition logi. 
Bootstrap purposes, obtained via [CDN](https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css) was not validated through JSHint.

| Page | Screenshot | Errors | Warnings |
| ---- | ------ | ------ | ------ | 
| comment.js | ![comments](documentation/images/27_javascript_comments.png) | none | 2 |
| terms.js | ![terms](documentation/images/26_javascript_terms.webp) | none | none |


jshint - comment.js

Warnings addressed - for this project this would surfice but can be addressed in a later feature:

1. If blogSlug never changes, you can safely ignore the warning.
2. If you plan to maintain or scale the code, refactoring as shown above will make it cleaner and future-proof.


<hr>

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com) -used for the validation of Python files in my project, due to having 3 apps this turned out to be a more complex process with a lot of moving parts, however no issues. Screenshots included below.

| Feature | admin.py | forms.py | models.py | urls.py | views.py | test.py | apps.py | signals.py |
| ---- | ---- | ------- | ------ | ----- | -----| ------ | ----- | -----|
| Main | n/a | n/a | n/a | [No Errors](documentation/testing/23_pl_main_urls.webp) | n/a | n/a  |  n/a  |  n/a  |
| Blog | [No Errors](documentation/testing/19_pl_blog_admin.webp) | [No Errors](documentation/testing/35_pl_blog_forms.webp) | [No Errors](documentation/testing/34_pl_blog_models.webp) | [No Errors](documentation/testing/32_pl_blog_urls.webp) | [No Errors](documentation/testing/31_pl_blog_views.webp) | [No Errors](documentation/testing/33_pl_blog_tests.webp) | [No Errors](documentation/testing/36_pl_blog_apps.webp) |  n/a  |
| Comments | [No Errors](documentation/testing/30_pl_comments_admin.webp) | [No Errors](documentation/testing/28_pl_comments_forms.webp) | [No Errors](documentation/testing/27_pl_comments_models.webp) | [No Errors](documentation/testing/25_pl_comments_urls.webp) | [No Errors](documentation/testing/24_pl_comments_views.webp) | [No Errors](documentation/testing/26_pl_comments_tests.webp) | [No Errors](documentation/testing/29_pl_comments_apps.webp) |  n/a  |
| Profile | [No Errors](documentation/testing/22_pl_profile_admin.webp) | [No Errors](documentation/testing/20_pl_profile_forms.webp) | [No Errors](documentation/testing/18_pl_profile_models.webp) | [No Errors](documentation/testing/15_pl_profile_urls.webp) | [No Errors](documentation/testing/14_pl_profile_views.webp) | [No Errors](documentation/testing/16_pl_profile_tests.webp) | [No Errors](documentation/testing/21_pl_profile_apps.webp) | [No Errors](documentation/testing/17_pl_profile_signals.webp) |



<hr> 

### Lighthouse Scores

Lighthouse tested on several different computers for effective research. This was done using chrome Incognito mode. As you can see there are some high scores for Accessibility and SEO [SEO is going to be a future feature though]. I am happy about these scores mixed in with other accessbility and compliance score this shows the attention to responsive, readers and keyboard actions.
The main issue was due to it being a blog: User images threw up the main errors and issues and as a future feature it would be good to look at ways to impliment an image convertor or image processor to deal with this on site automatically once a user uplaods. static images were uplaoded in the correct format and with webp or png.
The CDNs used for Bootstrap were also noted in the Lighthouse report as causing issue with performance.
<br> 
<br> 
Desktop Home Page

![Lighthouse Desktop home](documentation/testing/12_lh_desktop_home.png)

<br> 
<br> 
Desktop Blog Page

![Lighthouse Desktop paginated blogs](documentation/testing/13_lh_desktop_blog.webp)

<br> 
<br> 
Desktop Post Page

![Lighthouse Desktop blog post](documentation/testing/11_lh_desktop_post.png)

<br> 
<br> 
Best practice 

![Lighthouse best practice](documentation/testing/07_lh_best_practice.webp)

<br> 
<br> 
Mobile Home Page 

![Lighthouse Mobile home](documentation/testing/12_lh_desktop_home.png)
<br> 
<br>
Mobile Blog page 

![Lighthouse Mobile paginated blogs](documentation/testing/10_lh_mobile_blog.webp)

<br> 
<br> 
Mobile Post page

![Lighthouse Mobile blog post](documentation/testing/11_lh_desktop_post.png)
 
  
<hr>

### Wave Accisibility Evaluation 

![WAVE Web Accessibility Evaluation Tools](documentation/testing/06_wave.png)

The WAVE report inspected various areas of the site. I cleaned up a few issues due to use of Heading tags, redundant links or not having labels, however the whole site is now inspected:

| Feature | Errors | Contrast Errors | Alerts |
| ---- | ---- | ------- | ------ | 
| Home | 0 | 0 | 0 | 
| Base | 0 | 0 | 0 | 
| Toast | 0 | 0 | 0 |
| blog_form | 0 | 0 | 0 |
| blog_post | 0 | 0 | 0 |
| blog_list | 0 | 0 | 0 |
| blog_edit | 0 | 0 | 0 |
| blog_delete | 0 | 0 | 0 |
| blog_search | 0 | 0 | 0 |
| profile_form | 0 | 0 | 0 |
| profile_detail | 0 | 0 | 0 |
| profile_confirm_delete | 0 | 0 | 0 |
| signin | 0 | 0 | 0 |
| signout | 0 | 0 | 0 |
| signup | 0 | 0 | 0 |


### Accessible and Compliant checker

I also looked at the [Accessibility and Compliance checker](https://www.accessibilitychecker.org/), which is an accessible and compliant checker to make sure the site was inclusive and reached standards for inclusivity. Adding the url helps to find out the website is Accessible and Compliant, with ADA and WCAG compliance checking it identifies web accessibility issues and gives exact instructions for fixing them. No critical issues received:

![Acces Check](documentation/testing/04_access_check.png)
![Acces Check](documentation/testing/05_access_check.png)



## Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process the input appropriately.

| Feature | Tested? | User Input required | User Feedback Provided | Pass/Fail | Fix |
| ------- | ------- | ------------------- | ---------------------- | --------- | --- |
| Navbar | Yes | Click | The user is directed to the specific page as intended | Pass | - |
| Register Page | Yes | Username/Password. Email is optional | Empty username and password fields prompt the user. [username/password](documentation/testing/password_similar.png) too similar, password too short | Pass | - |
| Login | Yes | Username and Password | Username and Password must be exactly as originally registered. User notified once successfully signed in. | Pass | - |
| Search Field | Yes |Any input accepted but Search results are tailored to Location, Category, and Post title. | Users will be presented with the results of their search. If no results are found the user receives [this](documentation/testing/search_feedback.png) feedback | Pass | - |
| Blog Post Links | Yes | Click | User is taken to intended location via a new tab | Pass | - |
| Add Post (Registered User) | Yes | Mixture of image and text fields. | Business name, Post Content and Location are required fields. User is redirected back to the Business name field if not entered when trying to post. User receives [this](documentation/testing/add_post_mt_loc.png) if location field is blank. User receives [this](documentation/testing/add_post_mt_content.png) if content field is left blank. Once completed the User is notified that the Post will be published after it has been reviewed by the Happy Heath team | Pass | - |
| Comment Box (Registered User) | Yes | Text input accepted | User is thanked for their comment | Pass | - |
| Edit Comment (Registered, Author) | Yes | Click button to choose Edit | Comment appears in comment box for update and update button appears underneath. When pressed the user is infomred that the comment has been updated | Pass | - |
| Delete Comment (Registered, Author) | Yes | Click button to choose Delete comment | A [modal](documentation/testing/comment_delete_modal.png) pops up asking the user if they are sure they want to delete their comment | Pass | - |
| Edit Post (Registered, Author) | Yes | Image/Text fields | Changes made to post are saved and displayed. The user is informed that the post has been updated successfully | Pass | - |
| Delete Post (Registered, Author) | Yes | Click Confirm Delete button or cancel | Post is deleted and user is returned to home page | Pass | - |
| Log Out | Yes | Click Logout in the navigation menu | User is signed out and confirmation message appears at the top of the screen | Pass | - |
| Contact Form | Yes | Text Fields | Users will get [feedback](documentation/testing/contact_form_input_req.png) if they try to submiy without filling in the required fields. Once submitted successfully the user will receive a notification at the top of the page | Pass | - |
| Footer icons | Yes | Click | Icons take the user to the intended location via a new tab | Pass | - |

### Browser Compatibility 

Happy Heath was tested on the following browsers. New users were created and old users data edited. All features were tested and no issues found:

- Chrome v131.0.6778.86
- Edge v131.0.2903.51
- Safari v18.1.1

<hr>



















<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>