<template>
    <v-form
    ref="form"
    v-model="valid"
    lazy-validation
    >
  <v-container fluid fill-height>
    <v-row fill-height>
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
          :rules="requiredRules"
        ></v-textarea>

        

        
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        
        <v-textarea
          solo
          v-model="letters.content"
          maxlength="500"
          name="input-7-4"
          label="風船をReleaseしましょう"
          :rules="requiredRules"
        ></v-textarea>

      </v-col>


      <v-col
        cols="12"
        md="6"
      >

        <v-file-input
          accept="image/*"
          label="画像をアップロード"
          clearable
          v-model="letters.image"
        ></v-file-input>


      </v-col>

      

      <v-col
        cols="12"
        md="6"
      >

        <v-btn
          elevation="4"
          color="success"
          @click="release"
        >Release!</v-btn>


      </v-col>


    </v-row>
  </v-container>
  </v-form>
  
</template>



<script>
import axios from 'axios'
import router from '../router'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const formData = new FormData()


  export default {
    data: () => ({
      valid: true,
      loading:false,
      letters: {},
      select: null,
      requiredRules:[
        v => !!v || '入力必須の項目です',
        v => (v && v.length < 201) || "文字数は200字以内です",
      ]
    }),

    methods: {
      upimg(){
          
          formData.append("author", this.letters.author)
          formData.append("content", this.letters.content)
          if (this.letters.image){
              formData.append("image", this.letters.image)
          }        
      },
        




      release(){
        if (this.$refs.form.validate()){
          this.upimg()
          axios({
            method: 'POST',
                    url: 'http://localhost:8000/back_end/balloon/release/',
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    data: formData,
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                    mode: 'same-origin'
          })
            
            .catch(function (error) {
                if (error.response) {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                } else if (error.request) {
                console.log(error.request);
                } else {
                console.log('Error', error.message);
                }
                console.log(error.config);
            });
            
            router.push('/postlist');
          
        }
      }
    }

    }
  
</script>