// const URL_API = 'http://localhost:3333';
const URL_API = 'https://service-flask-rest-api.herokuapp.com';

// eslint-disable-next-line no-undef
let app = new Vue({
  el: '#app',
  data: {
    title: 'Welcome to Flask Api Service',
    subTitle: '** With this service, waste can be sorted by giving an image.**',
    showImage: false,
    imageUri: '',
    imageName: '',
    fileImage: null,
    response: null,
    loading: false,
    error: null,
  },
  methods: {
    onPickImage: function () {
      this.$refs['input-file'].click();
    },
    onSendImage: async function () {
      this.response = null;
      let formData = new FormData();
      formData.append('file', this.fileImage);
      this.loading = true;
      this.error = null;
      try {
        let data = await fetch(`${URL_API}/image/analyze`, {
          body: formData,
          method: 'POST',
        });
        if (data.status > 399) {
          let resp = await data.json();
          throw new Error(resp.message);
        }
        this.loading = false;
        this.response = await data.json();
      } catch (e) {
        this.loading = false;
        this.error = e.message;
      }
    },
    ///////////////////IMAGE PICKER FUNCTIONALITIES //////////////////////////////
    onHandleFileSelect: function (evt) {
      const files = evt.target?.files;
      if (files) {
        const file = files[0];
        this.imageName = file.name.split('.')[0];
        this.imageUri = `data:${file.type};base64,`;
        this.fileImage = file;
        if (files && file) {
          const reader = new FileReader();
          reader.onload = this.handleReaderLoaded.bind(this);
          reader.readABinaryString(file);
        }
      }
    },
    handleReaderLoaded: function (readerEvt) {
      const binaryString = readerEvt.target.result;
      const base64textString = btoa(binaryString);
      this.imageUri += base64textString;
      this.showImage = true;
    },
    calculateSize: function () {
      if (this.imageUri && this.imageUri.length) {
        return Math.ceil(((3 / 4) * this.imageUri.length) / 1024);
      } else {
        return;
      }
    },
  },
  created() {
    console.log('Hello I have the control');
  },
});