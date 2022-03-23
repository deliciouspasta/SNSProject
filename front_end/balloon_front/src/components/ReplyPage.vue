<template>
    <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    >
  <v-container fluid>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-textarea
          solo
          v-model="letters.author"
          maxlength="50"
          name="input-7-4"
          label="名前"
          required
        ></v-textarea>

        <v-btn
          elevation="4"
          @click="release"
        >Release!</v-btn>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
      </v-col>

      <v-textarea
          solo
          v-model="letters.content"
          maxlength="500"
          name="input-7-4"
          label="風船をReleaseしましょう"
          required
        ></v-textarea>

      <v-col
        cols="12"
        md="6"
      >
      </v-col>

    </v-row>
  </v-container>
  </v-form>
  
</template>



<script>
import axios from 'axios'
import router from '../router'
// import Cookies from 'js-cookie'

// const csrftoken = Cookies.get('csrftoken')
// const doc = document
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

if (csrftoken){
    console.log("succsses!!!")
    // console.log(csrftoken)
}else{
    console.error("csrftoken does not exist")
}

  export default {
    data: () => ({
      valid: true,
      loading:false,
      letters: {},
      select: null,
    }),

    methods: {

        




      release(){
        // console.log(res.data.name + res.data.content)
        if (this.$refs.form.validate()){
          axios({
            method: 'POST',
                    url: 'http://localhost:8000/back_end/balloon/release/',
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    data: this.letters,
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    mode: 'same-origin'



          }).then(res => {
              this.$router.push({author:res.data.name, content:res.data.content})
              console.log(res.data.name + res.data.content)
              router.push('/balloonpage');
            })
            
            .catch(function (error) {
                if (error.response) {
                // 要求がなされたとサーバがステータスコードで応答した
                // 2XXの範囲外
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                } else if (error.request) {
                // 要求がなされたが、応答が受信されなかった
                // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                // http.ClientRequest in node.js
                console.log(error.request);
                } else {
                // トリガーしたリクエストの設定に何かしらのエラーがある
                console.log('Errorrrrr', error.message);
                }
                console.log(error.config);
                // console.log(csrftoken);
            });
            
            
          
        }
      }
    }

    



}
  
</script>