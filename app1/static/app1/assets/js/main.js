
"use strict";

//Variables
const MOBILE_POINT = 768;
const slideArrow = {
  nextArrow: `<button type="button" class="slick-next"><i class="fas fa-chevron-right"></i></button>`,
  prevArrow: `<button type="button" class="slick-prev"><i class="fas fa-chevron-left"></i></button>`,
};
const DUMMY_DATA = [
  {
    image: "assets/images/posts/react.jpg",
    category: "Web Development",
    title: "Why You Should Be Using React",
    date: "Clock  Wed 02, 2020",
    comment: 3,
  },
  {
    image: "assets/images/posts/ecommerce.jpg",
    category: "Web Development",
    title: "Ecommerce Development Trends",
    date: "Clock  Wed 02, 2020",
    comment: 3,
  },
  {
    image: "assets/images/posts/react.jpg",
    category: "Web Development",
    title: "Should you Learn React",
    date: "Clock  Wed 02, 2020",
    comment: 3,
  },
  {
    image: "assets/images/posts/ecommerce.jpg",
    category: "Web Development",
    title: "Ecommerce Development Trends",
    date: "Clock  Wed 02, 2020",
    comment: 3,
  },
  {
    image: "assets/images/posts/react.jpg",
    category: "Web Development",
    title: "Why You Should Be Using React",
    date: "Clock  Wed 02, 2020",
    comment: 3,
  },
  {
    image: "assets/images/posts/ecommerce.jpg",
    category: "Web Development",
    title: "Ecommerce Development Trends",
    date: "Clock  Wed 02, 2020",
    comment: 3,
  },
  {
    image: "assets/images/posts/react.jpg",
    category: "Web Development",
    title: "Why You Should Be Using React",
    date: "Clock  Wed 02, 2020",
    comment: 3,
  },
];

let currentCategoryLayout = "";

//==========================================
//  Utilities
//==========================================
function onMobileBreakpoint(less, than) {
  if (window.matchMedia(`(max-width: ${MOBILE_POINT}px)`).matches) {
    less();
  } else {
    than();
  }
}

function onResizeBreakpoint(less, than) {
  onMobileBreakpoint(less, than);
  $(window).on("resize", function () {
    onMobileBreakpoint(less, than);
  });
}

function clickOutSideElm(elm, callback) {
  $(document).mouseup(function (e) {
    var container = $(elm);
    if (!container.is(e.target) && container.has(e.target).length === 0) {
      callback();
    }
  });
}
//==========================================
//==========================================

//Category post generator
function categoryGenerator() {
  function getLayout() {
    let $activeCategoryItem = $(".category__header__filter__item.active");
    const currentLayout = $activeCategoryItem.data("layout");
    let content = "";
    if (currentCategoryLayout === currentLayout) {
      return;
    }
    currentCategoryLayout = currentLayout;
    if (currentCategoryLayout === "grid") {
      DUMMY_DATA.forEach((item, index) => {
        content += `
          
        `;
      });

      $categoryContent
        .empty()
        .addClass("-grid")
        .removeClass("-list")
        .prepend(content);
      let $masonryBeauty = $categoryContent.masonry({
        itemSelector: ".post-card",
        gutter: 20,
      });
      $masonryBeauty.imagesLoaded().progress(function () {
        $masonryBeauty.masonry("layout");
      });
    } else {
      $categoryContent.masonry("destroy");
      DUMMY_DATA.forEach((item, index) => {
        content += `
        <div class="col-12">
          <div class="post-card -small -horizontal">
            <a class="card__cover" href="post.html" tabindex="0"><img src="${item.image}" alt="${item.title}"></a>
            <div class="card__content">
              <h5 class="card__content-category">Web Development</h5>
                <a class="card__content-title" href="post.html" tabindex="0">${item.title}</a>
              <div class="card__content-info">
                <div class="info__time"><i class="far fa-clock"></i>
                  <p>Clock  Wed 02, 2020</p>
                </div>
                <div class="info__comment"><i class="far fa-comment"></i>
                  <p>3</p>
                </div>
              </div>
              <p class="card__content-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt labore aliqua. Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis.</p>
            </div>
          </div>
        </div>`;
      });
      content = `<div class="row">${content}</div>`;
      $categoryContent
        .empty()
        .addClass("-list")
        .removeClass("-grid")
        .prepend(content);
    }
  }

  getLayout();

  $(".category__header__filter__item").on("click", function (e) {
    e.preventDefault();
    $(".category__header__filter__item").removeClass("active");
    $(this).addClass("active");
    getLayout();
  });
}

//Nav dropdown handle
function navDropdownHandle() {
  let header = $("header");
  let nav = $("header nav");

  function dropdownMenuMobileHandle() {
    if ($(".nav-item").children(".dropdown-menu__controller").length > 0) {
      return;
    }
    $(".nav-item:has(.dropdown-menu)").prepend(
      `<a href="#" class="dropdown-menu__controller"><i class="fas fa-plus"></i></a>`
    );

    $(".dropdown-menu__controller").on("click", function (e) {
      e.preventDefault();
      $(this)
        .parent()
        .siblings()
        .children(".dropdown-menu")
        .removeClass("show");
      $(this).siblings(".dropdown-menu").toggleClass("show");
      $(".dropdown-menu__controller i")
        .removeClass("fa-minus")
        .addClass("fa-plus");
      if ($(this).siblings(".dropdown-menu").hasClass("show")) {
        $(this).children().removeClass("fa-plus").addClass("fa-minus");
      } else {
        $(this).children().removeClass("fa-minus").addClass("fa-plus");
      }
    });
  }

  function dropdownMenuDesktopHandle() {
    $(".dropdown-menu__controller").remove();
    $(".dropdown-menu").removeClass("show");
  }

  //Mobile menu handle
  function menuMobileHandle() {
    header.addClass("is-mobile");
    nav.slideUp();
    dropdownMenuMobileHandle();
  }
  //Desktop menu handle
  function menuDesktopHandle() {
    header.removeClass("is-mobile");
    nav.removeAttr("style");
    dropdownMenuDesktopHandle();
  }

  onResizeBreakpoint(menuMobileHandle, menuDesktopHandle);

  (function () {
    $("#mobile-menu-controller").on("click", function (e) {
      e.preventDefault();
      nav.slideToggle();
    });
  })();
}

//Menu scroll handle
function menuScrollHandle() {
  let header = $("header");
  $(window).on("scroll", function (e) {
    let topPos = $(this).scrollTop();
    if (topPos > 200) {
      header.addClass("scroll-down");
    } else {
      header.removeClass("scroll-down");
    }
  });
}

//Show search input
function showSearchInput() {
  let isOpened = false;
  let $searchBox = $("#search-box");
  $searchBox.slideUp();
  $("#search").on("click", function (e) {
    e.preventDefault();
    if (!isOpened) {
      $searchBox.slideDown();
      isOpened = true;
      $(this).addClass("active");
    } else {
      $searchBox.slideUp();
      isOpened = false;
      $(this).removeClass("active");
    }
  });
  clickOutSideElm($("header"), function () {
    $searchBox.slideUp();
    isOpened = false;
    $("#search").removeClass("active");
  });
}

//Slide init
function ititalSlide() {
  $(".card__cover.-slide").slick(
    Object.assign({ slidesToShow: 1, slidesToScroll: 1 }, slideArrow)
  );

  $(".card__cover.-slide-splited").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: false,
    responsive: [
      {
        breakpoint: 996,
        settings: {
          slidesToShow: 2,
        },
      },
    ],
  });

  $(".blog-imageless-mansonry__categories").slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    arrows: false,
    responsive: [
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 4,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 3,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 2,
        },
      },
    ],
  });

  if ($(".instagrams-container").parents(".container").length > 0) {
    $(".instagrams-container").slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      arrows: false,
      autoplay: true,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 4,
          },
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 3,
          },
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 2,
          },
        },
      ],
    });
  } else {
    $(".instagrams-container").slick({
      slidesToShow: 6,
      slidesToScroll: 1,
      arrows: false,
      autoplay: true,
      responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 5,
          },
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 4,
          },
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 3,
          },
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 2,
          },
        },
      ],
    });
  }

  $(".blog-ocean__slider").slick(Object.assign({ fade: true }, slideArrow));

  $(".news-block__tab__item.active .news-block__content").slick(
    Object.assign({ infinite: false }, slideArrow)
  );

  $(".news-block__tab__item.active .news-block__content-multi").slick(
    Object.assign(
      {
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 3,
            },
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 576,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      },
      slideArrow
    )
  );

  $(".blog-food__slide").slick(
    Object.assign(
      {
        slidesToShow: 5,
        slidesToScroll: 1,
        responsive: [
          {
            breakpoint: 1200,
            settings: {
              slidesToShow: 4,
            },
          },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 3,
            },
          },
          {
            breakpoint: 695,
            settings: {
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 465,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      },
      slideArrow
    )
  );

  $(".blog-flower__slide").slick(
    Object.assign(
      {
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [
          {
            breakpoint: 1400,
            settings: {
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      },
      slideArrow
    )
  );

  $(".related-post-slide").slick(
    Object.assign(
      {
        slidesToShow: 4,
        slidesToScroll: 1,
        arrows: false,
        responsive: [
          {
            breakpoint: 996,
            settings: {
              arrows: true,
              slidesToShow: 3,
            },
          },
          {
            breakpoint: 768,
            settings: {
              arrows: true,
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 576,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      },
      slideArrow
    )
  );

  function slideSync() {
    $(".slider-single").slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: false,
      adaptiveHeight: true,
      infinite: false,
      useTransform: true,
      speed: 400,
      cssEase: "cubic-bezier(0.77, 0, 0.18, 1)",
    });

    $(".slider-nav")
      .on("init", function (event, slick) {
        $(".slider-nav .slick-slide.slick-current").addClass("is-active");
      })
      .slick(
        Object.assign(
          {
            slidesToShow: 3,
            slidesToScroll: 3,
            dots: false,
            focusOnSelect: false,
            infinite: false,
          },
          slideArrow
        )
      );

    $(".slider-single").on("afterChange", function (
      event,
      slick,
      currentSlide
    ) {
      $(".slider-nav").slick("slickGoTo", currentSlide);
      var currrentNavSlideElem =
        '.slider-nav .slick-slide[data-slick-index="' + currentSlide + '"]';
      $(".slider-nav .slick-slide.is-active").removeClass("is-active");
      $(currrentNavSlideElem).addClass("is-active");
    });

    $(".slider-nav").on("click", ".slick-slide", function (event) {
      event.preventDefault();
      var goToSingleSlide = $(this).data("slick-index");

      $(".slider-single").slick("slickGoTo", goToSingleSlide);
    });
  }

  slideSync();
}

//Plyr init
function plyrInit() {
  const audioPlayer = Plyr.setup(".audio", {
    controls: [
      "play-large",
      "play",
      "progress",
      "current-time",
      "mute",
      "volume",
    ],
  });

  const players = Array.from(document.querySelectorAll(".video")).map((p) => {
    return new Plyr(p, {
      controls: [
        "play-large",
        "play",
        "progress",
        "current-time",
        "mute",
        "volume",
        "fullscreen",
      ],
      hideControls: false,
      ratio: "16:9",
      vimeo: {
        byline: false,
        title: true,
      },
    });
  });

  players.forEach((item) => {
    item.toggleControls(false);
    item.on("play", (event) => {
      item.toggleControls(true);
    });
    let videoTitle = $(item.elements.container).siblings("a");
    if (videoTitle) {
      item.on("playing", (event) => {
        videoTitle.hide();

        item.toggleControls(true);
      });
    }
  });

  const verticalPlayers = Array.from(
    document.querySelectorAll(".video-9x16")
  ).map((p) => {
    return new Plyr(p, {
      controls: [
        "play-large",
        "play",
        "progress",
        "current-time",
        "mute",
        "volume",
        "fullscreen",
      ],
      hideControls: false,
      ratio: "9:16",
      vimeo: {
        byline: false,
        title: true,
      },
    });
  });

  verticalPlayers.forEach((item) => {
    item.toggleControls(false);
    item.on("play", (event) => {
      item.toggleControls(true);
    });
    item.source = {
      poster: "../images/backgrounds/trending-post-1.png",
    };
    let videoTitle = $(item.elements.container).siblings("a");
    console.log(videoTitle);
    if (videoTitle) {
      item.on("playing", (event) => {
        videoTitle.hide();

        item.toggleControls(true);
      });
    }
  });

  const videoListPlayer = new Plyr("#video-list-player", {
    controls: [
      "play-large",
      "play",
      "progress",
      "current-time",
      "mute",
      "volume",
      "fullscreen",
    ],
    ratio: "16:9",
  });

  let $h2Tag = $(videoListPlayer.elements.container).siblings("h2");
  videoListPlayer.on("play", (event) => {
    $h2Tag.hide();
  });
  videoListPlayer.on("pause", (event) => {
    $h2Tag.show();
  });

  $(".video-list__content__item").on("click", function (e) {
    e.preventDefault();
    let src = $(this).data("src");
    let type = "video/mp4";
    let provider = "vimeo";
    let title = $(this).find(".item__detail h5").text();

    $("#video-list__title").text(title);

    $(this).addClass("active").siblings().removeClass("active");

    $("#video-list__title").text();
    videoListPlayer.source = {
      title: "Test",
      type: "video",
      sources: [
        {
          src: src,
          provider: "vimeo",
        },
      ],
    };
  });
}

//Mansonry layout init {
function masonry() {
  let $masonry = $(".blog-masonry").masonry({
    itemSelector: ".post-card",
    horizontalOrder: true,
    gutter: 30,
  });

  $masonry.imagesLoaded().progress(function () {
    $masonry.masonry("layout");
  });

  let $masonryBeauty = $(".blog-imageless-mansonry__content").masonry({
    itemSelector: ".post-card",
    gutter: 20,
    // fitWidth: true,
    // percentPosition: true,
  });

  $masonryBeauty.imagesLoaded().progress(function () {
    $masonryBeauty.masonry("layout");
  });

  let $masonryBeauty2 = $(".blog-imageless-mansonry__content__wide").masonry({
    itemSelector: ".grid-item ",
    // gutter: 20,
    // fitWidth: true,
    columnWidth: ".grid-sizer",
    percentPosition: true,
  });

  $masonryBeauty2.imagesLoaded().progress(function () {
    $masonryBeauty2.masonry("layout");
  });
}

//Tab
function tab() {
  (function newsBlockTab() {
    $(".tab-item").on("click", function (e) {
      e.preventDefault();
      $(this).addClass("active").siblings().removeClass("active");

      let getShownTab = $(this).data("for");
      let foundTab = $(this)
        .parents(".news-block__header")
        .siblings(".news-block__tab")
        .find(`[data-tab-name='${getShownTab}']`);
      let foundSlide = foundTab.find(".news-block__content");
      foundTab.fadeIn(300).siblings().fadeOut(300).removeClass("active");
      foundSlide.slick(Object.assign({ infinite: false }, slideArrow));
    });
  })();
  (function tabHandle() {
    let dataFor = $(".tab-header ul>li>a.active").data("for");

    $(`.tab .tab-content__item[data-stand="${dataFor}"]`).addClass("active");

    $(".tab-header ul>li>a").on("click", function (e) {
      e.preventDefault();
      let currentDataFor = $(this).data("for");
      $(".tab-header ul>li>a").removeClass("active");
      $(".tab-content__item").removeClass("active");
      $(this)
        .addClass("active")
        .parents(".tab-header")
        .next()
        .find(`.tab-content__item[data-stand="${currentDataFor}"]`)
        .addClass("active");
    });
  })();
}

//Render product rate star
function renderStar() {
  const star = $(".star");
  const starHtml = '<i class="fas fa-star"></i>';
  $.each(star, function (index, val) {
    const numberStar = $(val).data("number");
    $(val).prepend(starHtml.repeat(numberStar));
  });
}

//Change quantity
function quantityController() {
  const $up = $(".quantity-controller .increase-btn");
  const $down = $(".quantity-controller .decrease-btn");
  const $inputVal = $(".quantity-controller input").val();

  function pad(d) {
    return d < 10 ? "0" + d.toString() : d.toString();
  }

  function numberControl(e) {
    e.preventDefault();
    let val = $(this).siblings("input").val();

    if ($(this).hasClass("increase-btn")) {
      $(this)
        .siblings("input")
        .val(pad(parseInt(val) + 1));
    } else {
      if (val > 1) {
        $(this)
          .siblings("input")
          .val(pad(parseInt(val) - 1));
      }
    }
  }

  $up.on("click", numberControl);
  $down.on("click", numberControl);
}

//Select payment method
function selectPaymentMethod() {
  let $checkbox = $('.total__payment-method__block input[type="checkbox"]');

  function checkChecked() {
    $.each($checkbox, function (index, val) {
      if ($(val).is(":checked")) {
        $(val).parent().next().slideDown();
      } else {
        $(val).parent().next().slideUp();
      }
    });
  }

  checkChecked();
  $checkbox.on("click", checkChecked);
}

//Document ready
$(document).ready(function () {
  ititalSlide();
  navDropdownHandle();
  menuScrollHandle();
  showSearchInput();
  plyrInit();
  masonry();
  tab();
  renderStar();
  quantityController();
  selectPaymentMethod();
  //Preload
});

(function preload() {
  const $load = $("#load");
  $(window).on("load", function () {
    $load.fadeOut(300, function () {
      $load.remove();
    });
  });
})();
