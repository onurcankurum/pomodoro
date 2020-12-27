$(document).ready(function(){
    var countS = 25;
    $("#session").html(countS);
    var countB = 5;
    $("#break").html(countB);
    var pos = "pomodoro";
    var countLama;
    var posLama;
    var count;
    $("#stats").html(pos);
    var clock = $(".timer").FlipClock(0, {
      countdown: true,
      clockFace: 'MinuteCounter',
      autoStart: false,
      callbacks: {
        interval: function(){
          if (clock.getTime() == 0){
           /* if (pos == "session"){
              clock.setTime(countB*60);   // burası sadece zaman sıfırlanınca çalışır
              clock.start();
              pos = "break";
              $("#stats").html(pos);
            } else if (pos == "break"){
              clock.setTime(countS*60);
              clock.start();
              pos = "start";
              $("#stats").html(pos);
            }*/
          }
        }
      }
    })
    //SESSION
    $("#sessInc").on("click", function(){
      if ($("#session").html() > 0){
        countS = parseInt($("#session").html());
        countS+=1;
        $("#session").html(countS);
        //clock.setTime(countS*60);
      }
    });
    $("#sessDec").on("click", function(){
      if ($("#session").html() > 1){
        countS = parseInt($("#session").html());
        countS-=1;
        $("#session").html(countS);
        //clock.setTime(countS*60);
      }
    });
    //BREAK
    $("#breakInc").on("click", function(){
      if ($("#break").html() > 0){
        countB = parseInt($("#break").html());
        countB+=1;
        $("#break").html(countB);
      }
    });
    $("#breakDec").on("click", function(){
      if ($("#break").html() > 1){
        countB = parseInt($("#break").html());
        countB-=1;
        $("#break").html(countB);
      }
    });
    $("#start").on("click", function(){
      $("#title").text(count);
      if (count != countS || clock.getTime()==0){
        clock.setTime(countS*60);
        pos="session";
        $("#stats").html(pos);
      } else {
        pos = posLama;
        $("#stats").html(pos);
      }
      count = countS;
      clock.start();
    });
    $("#stop").on("click", function(){
      clock.stop();
      countLama = clock.getTime();
      posLama = $("#stats").html();
    });
    $("#clear").on("click", function(){
      clock.stop();
      pos = "pomodoro";
      $("#stats").html(pos);
      clock.setTime(0);
    });




    /* ===== Logic for creating fake Select Boxes ===== */
    $('.sel').each(function() {
      $(this).children('select').css('display', 'none');

      var $current = $(this);

      $(this).find('option').each(function(i) {
        if (i == 0) {
          $current.prepend($('<div>', {
            class: $current.attr('class').replace(/sel/g, 'sel__box')
          }));

          var placeholder = $(this).text();
          $current.prepend($('<span>', {
            class: $current.attr('class').replace(/sel/g, 'sel__placeholder'),
            text: placeholder,
            'data-placeholder': placeholder
          }));

          return;
        }

        $current.children('div').append($('<span>', {
          class: $current.attr('class').replace(/sel/g, 'sel__box__options'),
          text: $(this).text()
        }));
      });
    });

    // Toggling the `.active` state on the `.sel`.
    $('.sel').click(function() {
      $(this).toggleClass('active');
    });

    // Toggling the `.selected` state on the options.
    $('.sel__box__options').click(function() {
      var txt = $(this).text();
      var index = $(this).index();

      $(this).siblings('.sel__box__options').removeClass('selected');
      $(this).addClass('selected');

      var $currentSel = $(this).closest('.sel');
      $currentSel.children('.sel__placeholder').text(txt);
      $currentSel.children('select').prop('selectedIndex', index + 1);
    });




  });