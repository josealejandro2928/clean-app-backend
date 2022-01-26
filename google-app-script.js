function getDataFromExternalApi(imagePath) {
  let appName = 'CleanApp2-Pepe-testing-5347115';
  let tableName = 'Evidence';
  let fileName = imagePath;
  let urlImage = `https://www.appsheet.com/image/getimageurl?appName=${appName}&tableName=${tableName}&fileName=${fileName}`;

  var imgFileBlob = UrlFetchApp.fetch(urlImage).getBlob();

  let apiUrl = 'https://service-flask-rest-api.herokuapp.com/';
  let url = `${apiUrl}/image/analyze`;

  let options = {
    method: 'post',
    muteHttpExceptions: true,
    payload: {
      file: imgFileBlob,
    },
  };

  let resp = UrlFetchApp.fetch(`${url}`, options);
  return JSON.parse(resp.getContentText());
}

function getSuggestionLablesFromImage(fileName) {
  let data = getDataFromExternalApi(fileName);
  let labels = data['suggested_labels'].join(', ');
  return labels || 'None';
}

function getAccuracyTrashClass(fileName) {
  Utilities.sleep(1000);
  let data = getDataFromExternalApi(fileName);
  let trash_accuracy = data['trash']['accuracy'];
  Logger.log(trash_accuracy);
  return trash_accuracy.toFixed(2);
}
