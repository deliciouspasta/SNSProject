<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/balloonlogo.png">
    <h1>this is HOME!</h1>
    <h1 class="bg-secondary text-white display-4 px-3">Vue3</h1>
    <h1>{{ msg }}</h1>

    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>

    <router-link to="/" class="btn btn-primary mx-2">
        Go to Top
    </router-link>
    <router-link to="/balloonpage" class="btn btn-warning">
        Go to Balloon
    </router-link>

    <!-- <h2>ここに結果が表示 → {{ result }}</h2> -->
    <button class="btn btn-primary" @click="getAPI()">はじめる</button>
    <p class="display-1">{{msg}}</p>
    <div class="card" style="width:18rem;">
      <h5 class="cart-title">Balloonとは</h5>
      <p class="cart-text">サービスです</p>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  data () {
    return {
      result: 'No Result',
      url: 'http://localhost:8000/back_end/balloon/get/'
    }
  },
  methods: {
    getAPI () {
      // this.result = "this is test"
      axios.get(this.url)
      .then(response => {
        this.result = response.data.message
      })



      // .catch(function(error){
      //   if (error.response){
      //     console.log(error.response.data)
      //     console.log(error.response.status)
      //   }
      // })
      // this.$axios({
      //   method : 'GET',
      //   url : this.url
      // }).then(response => {
      //   this.result = response.data.message
      // })

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


</style>
