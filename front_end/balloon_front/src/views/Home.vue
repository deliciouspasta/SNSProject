<template>
  <div class="home">
    <v-container class="my-5">
    <div style="text-align: center; padding: 15px;">
      <img alt="Vue logo" src="../assets/balloonlogo.png">
    </div>

<v-spacer></v-spacer>
<v-spacer></v-spacer>
<v-spacer></v-spacer>
<v-spacer></v-spacer>
<v-spacer></v-spacer>
<v-spacer></v-spacer>
<v-spacer></v-spacer>

    <v-card
    class="mx-auto my-10"
    max-width="1000"
  >
    <v-img
      src="../assets/balloonsky.jpg"
      height="200px"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      
    ><v-card-title
      class="white--text font-weight-bold"
      max-width="2000"
    >Balloonとは</v-card-title>
    </v-img>
    
    
    <v-card-title>
      <p class="font-weight-bold">日々のつぶやきを投稿できるサービスです。
                投稿した内容は、

      いつ誰に届くかわからないバルーンレターのように、

      投稿日に関係なくランダムで表示されます。</p>
      
    </v-card-title>

  </v-card>



   <v-card
    class="mx-auto my-10"
    max-width="1000"
  >
    <v-img
      src="../assets/samplepost.png"
      height="200px"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
      
    ><v-card-title
      class="white--text font-weight-bold"
      max-width="2000"
    >どうでも良いことを、どうでも良いときに</v-card-title>
    </v-img>
    
    
    <v-card-title>
        <p class="font-weight-bold">何をつぶやけばいいのか悩んでいませんか？ご安心ください！何をつぶやいてもいいんです。</p>
    </v-card-title>

  </v-card>


    <v-card
    class="mx-auto my-10"
    max-width="1000"
    >
    <v-img
      src="../assets/sunset.jpg"
      height="200px"
      max-width="2000"
      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
    ><v-card-title
      class="white--text font-weight-bold"
    >さあ、始めましょう。</v-card-title>
    </v-img>


  </v-card>

  <div class="text-center">

      <v-row>

        <v-col>

          <v-btn
            class="white--text md-6"
            rounded
            color="primary"
            block
            to="/postlist"
            
          >
            会員登録せず始める
          </v-btn>
          </v-col>
          
          <v-col>
          <v-btn
            class="white--text md-6"
            rounded
            block
            color="error"
            to="/auth"
          >
          会員登録して始める
      </v-btn>

        </v-col>

      </v-row>

     

    </div>





  </v-container>
  </div>

</template>


<script>
export default {
  name: 'Home',
  props: {
    msg: String
  },

  data () {
    return {
      result: 'No Result',
      url: 'http://localhost:8000/back_end/balloon/get/'
    }
  },


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.full {
  margin: 0 calc(50% - 50vw);
}


</style>
