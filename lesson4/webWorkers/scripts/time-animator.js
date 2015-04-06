(function(){

  var canvas, context;

  init();
  requestAnimationFrame(animate);

  function init() {
    canvas = document.createElement( 'canvas' );
    canvas.width = 400;
    canvas.height = 200;
    context = canvas.getContext( '2d' );
    document.querySelector('#time-animation').appendChild( canvas );
  }

  function animate() {
    drawTime();
    requestAnimationFrame(animate);
  }

  var lastDiff = 0;
  var lastTime = 0;
  var displayTime = 0;
  var alpha = 1;
  var changeTime = 0;

  function drawTime() {

    var days = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday"
    ]

    var months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December"
    ]

    var now = new Date(Date.now());

    var year = now.getYear();
    var month = now.getMonth();
    var date = now.getDate();
    var day = now.getDay();
    var hours = now.getHours();
    var mins = now.getMinutes();
    var secs = now.getSeconds();
    var ms = now.getMilliseconds();

    var dateString = days[day] + ", " + date + " " + months[month] + " " + parseInt(1900 + year);

    var timeString = hours + ":" + mins + ":" + secs + ":" + ms;
    
    if (lastTime > 0) {
      frameTimeDiff = now - lastTime;
    } else {
      frameTimeDiff = null;
    }

    // threshold for shown jank is >50ms
    if (frameTimeDiff > lastDiff && frameTimeDiff > 50) {
      displayTime = frameTimeDiff;
      changeTime = now;
      alpha = 1;
    }

    context.clearRect(0,0, canvas.width, canvas.height);


    context.font = '24px sans-serif';
    context.fillStyle = 'rgba(41,72,96,1)';
    context.fillText("Date: " + dateString, 0, 50);
    context.fillText("Time: " + timeString, 0, 75);

    // fade out the "Jank Spotted" timer
    if (changeTime !== 0 && now - changeTime > 5000 && alpha > 0) {
      alpha = alpha - 0.05;
    }

    context.font = '36px sans-serif';
    context.fillStyle = 'rgba(41,72,96,' + alpha + ')';
    if (displayTime > 0) {
      context.fillText("Jank spotted: " + displayTime + "ms", 0, 125);
    }

    lastTime = now;
    lastDiff = frameTimeDiff;
  };
})();