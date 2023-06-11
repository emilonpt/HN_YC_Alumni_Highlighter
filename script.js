function changeColor(usernames){
  var links = document.querySelectorAll('a.hnuser');
  links.forEach(link => {
    if (usernames.includes(link.textContent)) {
      link.classList.add('ycalumni');
    }
  })}


let url = 'https://gist.githubusercontent.com/emilonpt/4042c34b5214eadd6d875c23c16f2838/raw/efe121e7ac566205c0ae044d8b49f2a90f5981dd/usernames.txt'; // replace with your actual URL

fetch(url)
    .then(response => response.text())
    .then(data => {
        let usernames = data.split('\n').filter(Boolean); // split by newline and filter out empty strings

        //change colour
        changeColor(usernames);
    })
    .catch(error => console.error('Error:', error));