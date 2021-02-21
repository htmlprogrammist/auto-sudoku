function render() {
  let main = document.querySelector('main');
  document.querySelector('button').addEventListener('click', (e) => {
    e.preventDefault();
    let values = document.querySelectorAll('input').value;
    console.log(values)
  })
}

window.onload = function () {
  render();
};
