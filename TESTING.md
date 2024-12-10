


## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Due to using Jinja syntax such as '{% extends "base.html" %} I had to use a different approach to checking my HTML as the validator would show errors if copying the HTML direct from the files in the Happy Heath project. My method to check my HTML was as follows:

- Using the deployed version from Heroku I navigated to each page.
- Right clicking on the page brought up a options menu with the option to view the page source located at the bottom.
- The complete HTML code for that page will then appear in a separate window.
- Copy that code and paste into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, and then repeat the steps to revalidate.

![html validation](documentation/testing/validator_clear.png) 

All HTML pages were validated and the pages generated solely by myself received a 'No errors or warning to show' result as shown above.

Initially my searh function raised a [warning](documentation/testing/search_validation_error.png) for the role attribute in the search function. The sign up page raised 4 [warnings](documentation/testing/validation_register.png) which is due to Django allauth forms. [Errors](documentation/testing/validator_add_post.png) were raised on the add post page which were generated by Summernote. These [Errors](documentation/testing/validator_edit_post.png) were repeated with the edit post page. The errors on the add_post.html and edit_post.html were cleared after the removal of the summernote widget.

| HTML source Code/Page | Errors | Warnings |
| ---- | ----- | ------|
| Home | 0 | 0 |
| Blog page | 0 | 0 |
| Blog Post | 0 | 0 |
| About | 0 | 0 |
| Add post | 0 | 0 |
| Await approval | 0 | 0 |
| Edit post | 0 | 0 |
| Delete post | 0 | 0 |
| Register | 4 | 0 |
| Log in | 0 | 0 |
| Log out | 0 | 0 |

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

[CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python files that were created or edited by myself. No issues presented. I have included some screenshots with the results below.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
| ---- | ---- | ------- | ------ | ----- | -----|
| Config | n/a | n/a | n/a | [No Errors](documentation/testing/config_urls.png) | n/a |
| Blog | [No Errors](documentation/testing/blog_admin.png) | [No Errors](documentation/testing/blog_forms.png) | [No Errors](documentation/testing/blog_models.png) | [No Errors](documentation/testing/blog_urls.png) | [No Errors](documentation/testing/blog_views.png) |
| About | [No Errors](documentation/testing/about_admin.png) | [No Errors](documentation/testing/about_forms.png) | [No Errors](documentation/testing/about_models.png) | [No Errors](documentation/testing/about_urls.png) | [No Errors](documentation/testing/about_views.png) |

<hr>

### CSS Validation

Css validation was done through the jigsaw.w3 css validator with no errors:

![No Errors](documentation/images/25_css_valid.webp)

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


[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) used to validate the CSS file:






External CSS for Bootstrap, provided by [CDN](https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css) was not tested. 


  
<hr> 

### Lighthouse Scores

Lighthouse testing was carried out in Incognito mode to acheive the best result. Performance was lower than preferred due to the site being image heavy. Static images used in the sites design were saved in webp. Image types added by a site user are at there own discretion and could affect the score. The CDNs used for Bootstrap were also noted in the Lighthouse report as causing issue with performance. This report will be reviewed for future development of Happy Heath to raise this score.

![Lighthouse scores home](documentation/testing/home_lg.png)
*Desktop Home Page*  
  
![Lighthouse scores paginated blogs](documentation/testing/blog_lh.png)
*Desktop Paginated Blogs Page*

![Lighthouse scores blog post](documentation/testing/blog_post_lh.png)
*Desktop Blog Post Page*  
  
![Lighthouse scores about](documentation/testing/about_lh.png)
*Desktop About Page*
  
<hr>

### Wave Accisibility Evaluation 

![WAVE Web Accessibility Evaluation Tools](documentation/testing/wave-accissibilty.png)

The WAVE report tool was used to check accisibility and initially raised a number of contrast issues due to the shade of the background colour. This was amended to accomadate and clear the accisibility issues.

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