// Бургер при уменьшении экрана 920px
burger = document.querySelector('.burger')
nav_menuid = document.querySelector('#nav_menuid')

burger.addEventListener('click',function(){
nav_menuid.classList.toggle('flexdisplay')
burger.classList.toggle('burg_open')
})


// $(document).ready(function(){
// $('.cats').children('a').each(function() {
//   $(this).hover(function(){
//     $('div#'+$(this).attr('id')).toggle("flex");
//   })

// })
    // .hover(function(){
            
    // })
    // $(this).on('ready',function(event){
    //     $
    //     $('div#'+$(this).attr('id'))
    // })
    // .on('mouseleave', function() {
    //     $('div#'+$(this).attr('id')).removeClass("active_element");
    //   });
    // ;})


// Всплывающее меню открытие категорий
$('div#cat_1').addClass('active_element')
$('#cat_1').css({
    'background':'white'
})

$('.cats').children('a').each(function() {
    $(this).on('mouseenter',function(event){
        $('.cats').children('a').each(function(){
            $(this).css({
                'background':'unset'
            })
            $('div#'+$(this).attr('id')).removeClass('active_element')
        })
        $('div#'+$(this).attr('id')).toggleClass("active_element");
        $(this).css({
            'background':'white'
        })
    })


    // .on('mouseleave', function() {
    //     if ($('.subcat_block').on('mouseleave',function(){
    //         $('div#'+$(this).attr('id')).removeClass("active_element");
    //     }));
    //   });
    ;})

// В бургере открытие вкладки категории
$('.nav_menu').children('a').each(function() {
$(this).on('click',function(event){
    $('div#'+$(this).attr('id')).toggle('display')
});})

$(document).ready(function(){
$('.filter-checkbox').on('click',function(){
let filter_obj ={}

$('.filter-checkbox').each(function(){
let filt_value = $(this).val()

let filt_key = $(this).data('filter')
filter_obj[filt_key] = Array.from(document.querySelectorAll('input[data-filter=' + filt_key + ']:checked')).map(function(element){
return element.value
})
})
let id_tovar = $('.katalog-tovars').attr('id')
$.ajax({
url:'/filter-products/'+id_tovar,
data: filter_obj ,
dataType:'json',
beforeSend: function(){
},
success:function(response){
$('#filtered_tovars').html(response.data)
}
})
})
})


$(document).ready(function(){
$('.filter-checkbox1').on('click',function(){
let filter_obj ={}

$('.filter-checkbox1').each(function(){
let filt_value = $(this).val()

let filt_key = $(this).data('filter')
filter_obj[filt_key] = Array.from(document.querySelectorAll('input[data-filter=' + filt_key + ']:checked')).map(function(element){
return element.value
})
})
let brend_name = $('.katalog-tovars').attr('id')
$.ajax({
url:'/filter-products-brend/'+brend_name,
data: filter_obj ,
dataType:'json',
beforeSend: function(){
},
success:function(response){
$('#filtered_tovars').html(response.data)
}
})
})
})

$('.filter_button').on('click',function(){
    $('.filter').toggleClass('block')
})


// Ссылки для картинок
let img1=document.querySelector('.vkimg')
img1.addEventListener('click',function(){
location.href='#'
})

let img2=document.querySelector('.telegramimg')
img2.addEventListener('click',function(){
location.href='#'
})

let img3=document.querySelector('.whatsappimg')
img3.addEventListener('click',function(){
location.href='#'
})


// Слайдер брендов
$(document).ready(function(){
    const slider = $(".owl-carousel").owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        navText: [
            '<svg width="35" height="35" viewBox="0 0 24 24"><path d="M16.67 0l2.83 2.829-9.339 9.175 9.339 9.167-2.83 2.829-12.17-11.996z"/></svg>',
            '<svg width="35" height="35" viewBox="0 0 24 24"><path d="M5 3l3.057-3 11.943 12-11.943 12-3.057-3 9-9z"/></svg>'
          ],
        dots:false,
        autoplay:true,
        autoplayTimeout:1500,
        smartSpeed:1300,
        responsive:{
            200:{
                items:2
            },
            560:{
                items:3
            },
            800:{
                items:4
            },
            1200:{
                items:5
            },
            1500:{
                items:7
            }
        }
    });
});

// Слайдер Популярных товаров
$(document).ready(function(){
    const slider = $(".owl-carousel second").owlCarousel({
        nav:true,
        loop:true,
        items:3,
        margin:10,
        navText: [
            '<svg width="35" height="35" viewBox="0 0 24 24"><path d="M16.67 0l2.83 2.829-9.339 9.175 9.339 9.167-2.83 2.829-12.17-11.996z"/></svg>',
            '<svg width="35" height="35" viewBox="0 0 24 24"><path d="M5 3l3.057-3 11.943 12-11.943 12-3.057-3 9-9z"/></svg>'
          ],
        dots:true,
        autoplay:true,
        autoplayTimeout:3500,
        smartSpeed:1300,
        responsive:{
            600:{
                items:2
            },
            700:{
                items:4
            },
            1000:{
                items:5
            }   
        }
    });
})



