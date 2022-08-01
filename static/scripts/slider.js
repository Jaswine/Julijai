const sliderMain = new Swiper('.slider__main', {
  freeMode: true,
  centeredSlides: true,
  mousewheel:true,
  parallax: true,
  breakpoints: {
      0: {
          slidesPerView: 2.5, 
          spaceBetween: 20,
      },
      660: {
          slidesPerView: 3.5,
          spaceBetween: 50,
      }
  }

});

const sliderBg = new Swiper('.slider__bg', {
  freeMode: true,
  centeredSlides: true,
  parallax: true,
  slidesPerView: 3.5,
  spaceBetween: 50,
})

sliderMain.controller.control =sliderBg

let desc = document.querySelector(".pre__description");
sliderMain.on('slideChange', e => {
  sliderMain.activeIndex> 0 ? desc.classList.add('hidden') : desc.classList.remove('hidden')
})