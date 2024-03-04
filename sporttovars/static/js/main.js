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
// убирает переход по форме
$('#filtration_tovars').on('click',(e)=>{
if (e.target.id === 'price-filter'){
e.preventDefault()
}})
// убирает переход по форме конец

// убирает переход по форме
$('#filtration_tovars').on('click',(e)=>{
if (e.target.id === 'price-filter1'){
e.preventDefault()
}})
// убирает переход по форме конец

// В бургере открытие вкладки категории
$('.nav_menu').children('a').each(function() {
$(this).on('click',function(event){
    $('div#'+$(this).attr('id')).toggle('display')
});})

// Ajax фильтрация для товаров
$(document).ready(function(){
$('.filter-checkbox,#price-filter1').on('click',function(){
let filter_obj ={}

let min_price = $('#min_price').val()
let max_price = $('#max_price').val()
filter_obj.min_price = min_price;
filter_obj.max_price = max_price;
$('.filter-checkbox').each(function(){
let filt_value = $(this).val()

let filt_key = $(this).data('filter')
filter_obj[filt_key] = Array.from(document.querySelectorAll('input[data-filter=' + filt_key + ']:checked')).map(function(element){
return element.value
console.log(filt_key)
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
// Ajax фильтрация для товаров конец

// Ajax фильтрация для брендов
$(document).ready(function(){
$('.filter-checkbox1,#price-filter').on('click',function(){
let filter_obj ={}

let min_price = $('#min_price').val()
let max_price = $('#max_price').val()
filter_obj.min_price = min_price;
filter_obj.max_price = max_price;

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

// Ajax фильтрация для поиска
$(document).ready(function(){
$('.filter-checkbox2,#price-filter').on('click',function(){
let filter_obj ={}

let min_price = $('#min_price').val()
let max_price = $('#max_price').val()
filter_obj.min_price = min_price;
filter_obj.max_price = max_price;
$('.filter-checkbox2').each(function(){
let filt_value = $(this).val()

let filt_key = $(this).data('filter')
filter_obj[filt_key] = Array.from(document.querySelectorAll('input[data-filter=' + filt_key + ']:checked')).map(function(element){
return element.value
})
})
let id_search = $('.katalog_search').attr('id')
$.ajax({
url:'/filter-products-search/'+id_search,
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
// Ajax фильтрация для брендов конец

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



