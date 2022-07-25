const story__tops = document.querySelectorAll('.story__top');
const videos = document.querySelectorAll('video');
const stories = document.querySelectorAll('story');
const body = document.querySelector('body');
const story__pads = document.querySelectorAll('.story__pad');
const story__fields = document.querySelectorAll('.story__field');
const story__items = document.querySelectorAll('.story__item');
const post__navs = document.querySelectorAll('.post__nav');
const story__menus = document.querySelectorAll('.story__menu');

for (let i=0; i<stories.length; i++ ) {
    let story__top = story__tops[i];
    let video = videos[i];
    let story = stories[i];
    let story__pad = story__pads[i];
    let story__field = story__fields[i];
    let story__item = story__items[i];
    let post__nav = post__navs[i];
    let story__menu = story__menus[i]

    story__top.addEventListener('click', () => {
        //clases
        story.classList.add('full');
        video.classList.add('big-shadow');
        video.classList.add('story__video');
        story__field.classList.add('story__back');
        story__pad.classList.add('story__sistem');
        story__pad.classList.remove('post__border');
        // post__nav.classList.add('story__for__post__nav');
        story__menu.classList.remove('disp-n');
        story.style.zIndex = '1000';
        body.style.overflowY = 'hidden';
        story__item.style.justifyContent = 'center';

        if (video.controls != true) {
            video.controls = true ;
        }
    });

    story__field.addEventListener('click', () => {
        //classes
        story.classList.remove('full');
        video.classList.remove('big-shadow');
        video.classList.remove('story__video');
        story__field.classList.remove('story__back');
        story__pad.classList.remove('story__sistem');
        story__pad.classList.add('post__border');
        // post__nav.classList.remove('story__for__post__nav');
        story__menu.classList.add('disp-n');
        story.style.zIndex = '0';
        body.style.overflowY = 'auto';
        story__item.style.justifyContent = 'space-between';

        if (video.controls == true) {
            video.controls = false ;
        }
    });
}