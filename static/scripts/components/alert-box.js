Vue.component('app-alert-box', {
  template: `
      <div class="alert-box fade-in">
        <strong>Error!</strong>
        <slot></slot>
      </div>
    `,
});
