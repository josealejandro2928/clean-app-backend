Vue.component('app-navbar', {
  data: () => ({
    linkActivated: '/',
    title: 'ML Service'
  }),
  template: `
    <div class="toolbar" role="banner">
      <div class="container" style="display: flex; align-items: center;width:100%;height:100%;justify-content:space-between">
        <span style="display: flex;justify-content: center;align-items: center;">
          <img width="40" alt="App logo" src="static/images/python-svgrepo-com.svg"/>
          <h3 class="title">{{title}}</h3>
        </span>
       
        <span>
          <a  title="Waste classifier"  aria-label="Waste clf." rel="noopener" href="./" >
          <button :class="{navbtn:true,activated:(linkActivated == '/')}">Waste clf.</button>
          </a>
          <a title="Who are we?"  aria-label="About Us" rel="noopener" href="./about-us">
          <button :class="{navbtn:true,activated:(linkActivated == '/about-us')}">About Us</button>
          </a>
          <div class="spacer"></div>
        </span>
      </div>
    </div>
    `,
  created: function () {
    this.linkActivated = window.location.pathname;
  },
});
