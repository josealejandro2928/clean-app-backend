// const URL_API = 'http://localhost:3333';
const URL_API = 'http://cleanbackendapp-env.eba-cpumx2fm.us-east-1.elasticbeanstalk.com/';


// eslint-disable-next-line no-unused-vars
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
      try {
        this.error = null;
        const files = evt.target?.files;
        if (files) {
          const file = files[0];
          if (!file.type.includes(`image/`)) throw new Error("Images are only allowed");
          this.imageName = file.name.split('.')[0];
          this.imageUri = `data:${file.type};base64,`;
          this.fileImage = file;
          if (files && file) {
            const reader = new FileReader();
            reader.onload = this.handleReaderLoaded.bind(this);
            reader.readAsBinaryString(file);
          }
        }
      } catch (error) {
        this.error = error.message;
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
