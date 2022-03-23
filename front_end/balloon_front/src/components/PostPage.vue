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

const formData = new FormData()


  export default {
    data: () => ({
      valid: true,
      loading:false,
      letters: {},
      select: null,
    }),

    methods: {
      upimg(){
          
          formData.append("author", this.letters.author)
          formData.append("content", this.letters.content)
          if (this.letters.image){
              formData.append("image", this.letters.image)
          }
        //   formData.append("image", this.letters.image)          
      },
        




      release(){
        // console.log(res.data.name + res.data.content)
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
            
            router.push('/balloonpage');
          
        }
      }
    }

    

    // mounted: function(){
    
    //     // GET
    //     axios.get('http://localhost:8000/back_end/balloon/release')
    //     .then(response  => {
    //         if (response.status == 200){
    //             // リストデータ
    //             this.letters = response.data;
    //         }else{
    //             this.status = '初期情報が読み込めませんでした。';
    //         }
    //     }) 
    //     .catch(err => {
    //         this.status = err.message;
    //     });
    // },




    // methods: {
    
    //     // ---------------------
    //     //  Ajax通信(送信用)
    //     // ---------------------  
    //     run_ajax: function(method, url, data) {
        
    //     axios({
    //         method  : method,
    //         baseURL : url,
    //         data    : data,
    //         headers : {
    //         // JSON
    //         'Content-Type': 'application/json',
    //         // CSRFトークン 
    //         'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content') 
    //         }
    //     })
    //     .then(response  => {
    //         this.status = "サーバーからのメッセージ(" + 
    //                     this.formatConversion(new Date())  + ") ：" + response.data.msg;
                        
    //         // 新規登録時のみIDなどが返却される
    //         if(response.data.id){
            
    //         // 失敗
    //         if(response.data.id == "error"){
                
    //             // エラー制御は行っていないので各自で。
                
    //         // 成功  
    //         }else{
    //             // 先頭にアイテムを追加する 
    //             this.letters.unshift({author:response.data.name, content:response.data.content});    
    //         }
            
    //         // 更新/削除
    //         }else{
    //         // エラー制御は行っていないので各自で。
    //         }      
    //     }) 
    //     .catch(err => {
    //         this.status = err.message;
    //         console.log(doc);
    //     });
    //     },   
        
        
    //     handleInsert: function() {    
      
    //         if (this.letters){
                
    //             // Ajax
    //             this.run_ajax("POST",
    //                         "http://localhost:8000/api/" ,
    //                         this.letters
    //                         );
        
    //             this.letters = {}
    //         }   
    //     },
    // }


    // methods: {
    //   release(){
    //     if (this.$refs.form.validate()){
    //     //   axios.defaults.xsrfCookieName = 'csrf-token'
    //     //   axios.defaults.xsrfHeaderName = "X-CSRFToken"
    //       axios.defaults.headers.common = {
    //         "X-Requested-With": "XMLHttpRequest",
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content') ,
    //         // 'X-CSRFToken': csrftoken,
             
    //       }
    //       axios
    //         .post('http://localhost:8000/back_end/balloon/release/', this.letters)
    //         .then(res => {
    //           this.$router.push({author:res.data.name, content:res.data.content})
    //         })
    //         .catch(function (error) {
    //             if (error.response) {
    //             // 要求がなされたとサーバがステータスコードで応答した
    //             // 2XXの範囲外
    //             console.log(error.response.data);
    //             console.log(error.response.status);
    //             console.log(error.response.headers);
    //             } else if (error.request) {
    //             // 要求がなされたが、応答が受信されなかった
    //             // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
    //             // http.ClientRequest in node.js
    //             console.log(error.request);
    //             } else {
    //             // トリガーしたリクエストの設定に何かしらのエラーがある
    //             console.log('Error', error.message);
    //             }
    //             console.log(error.config);
    //             // console.log(csrftoken);
    //         });
    //     }
    //   }
    // }
    
    










    // methods: {
    //     release(){
    //         this.loading = true;
    //         axios.post('http://localhost:8000/back_end/balloon/release/', this.letter)
    //         .catch(error => console.log(error))
    //     },
    // },      
    
    //   reset () {
    //     this.$refs.form.reset()
    //   },

    }
  
</script>