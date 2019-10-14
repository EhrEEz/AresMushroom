$(document).ready(function(){
    $(window).on("scroll load", function() {
    var navHeight = 80;
          if ($(window).scrollTop() > navHeight) {
            $('nav.navpane.transparent').css('background', 'rgba(255,255,255,1)');
            $('nav.navpane.transparent a').css('color', '#738785');
            $('nav.navpane.transparent u').css('color', '#738785');
            $('nav.navpane.transparent ul .active').css('color', '#051E85');
            $('nav.navpane.transparent ul #logo-link').css('visibility', 'visible');
            $('nav.navpane.transparent ul #logo-link').css('width', 'auto');
            $('nav.navpane.transparent ul #logo-link').css('height', 'auto');
            $('nav.navpane.transparent ul #logo-link').css('padding', 'auto');
            $('.hero .transparent .sideline .bottom').css('color', 'rgba(255,255,255,0)');

          }
          else {
            $('nav.navpane.transparent').css('background', 'rgba(255,255,255,0)');
            $('nav.navpane.transparent a').css('color', 'white');
            $('nav.navpane.transparent u').css('color', 'white');
            $('nav.navpane.transparent ul .active').css('color', '#B7FFCD');
            $('nav.navpane.transparent ul #logo-link').css('visibility', 'hidden');
            $('nav.navpane.transparent ul #logo-link').css('width', '0');
            $('nav.navpane.transparent ul #logo-link').css('height', '0');
            $('nav.navpane.transparent ul #logo-link').css('padding', '0');
            $('.hero .transparent .sideline .bottom').css('color', 'rgba(255,255,255,0.8)');
          }
     });
 });
