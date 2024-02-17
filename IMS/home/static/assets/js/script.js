let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
  arrow[i].addEventListener("click", (e) => {
    let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
    arrowParent.classList.toggle("showMenu");
  });
}
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", () => {
  sidebar.classList.toggle("close");
});


// ------------------------ 
const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'doughnut',
  data: {
    //labels: [ 'Low Stock Items', 'All Item Group', 'All Items', 'Unconfirmed Items' ],
    datasets: [{
      label: ['Low Stock Items', 'All Item Group', 'All Items', 'Unconfirmed Items'],
      data: [3, 39, 190, 121],
      backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)',
        'rgb(255, 0, 0)'
      ],
      hoverOffset: 4
    }]
  }
});





