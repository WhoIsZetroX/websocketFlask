var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('my_topic', function(data) {
    document.getElementById('topic').innerText = 'Current topic: ' + data.topic;
});

document.addEventListener('DOMContentLoaded', function() {
  nextTopic.addEventListener('click', function() {
    fetch('http://localhost:8087/next_topic')
      //.then(response => { console.log(response.text()) })
      //.then(data => { console.log('Response data:', data) })
      //.catch(error => { console.error('Fetch error:', error) });
  });
  prevTopic.addEventListener('click', function() {
    fetch('http://localhost:8087/prev_topic')
  });
});

