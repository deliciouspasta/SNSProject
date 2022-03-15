<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/balloonlogo.png">

    <router-link to="/balloonpage" class="btn btn-primary mx-2">
        はじめる
    </router-link>

    <router-link to="/postlist" class="btn btn-primary mx-2">
        これpostlist
    </router-link>

    <!-- <h2>ここに結果が表示 → {{ result }}</h2> -->
    <button class="btn btn-primary" @click="getAPI()">はじめる</button>
    <p class="display-1">{{msg}}</p>
    <!-- <div class="card" style="width:18rem;">
      <h5 class="cart-title">Balloonとは</h5>
      <p class="cart-text">サービスです</p>
    </div> -->

    <div class="card-deck">
      <div class="card" style="width: 54rem;">
        <svg class="bd-placeholder-img card-img-top" width="300%" height="180" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Image cap"><title>Placeholder</title><rect fill="#868e96" width="100%" height="100%"/><text fill="#dee2e6" dy=".3em" x="50%" y="50%">Image cap</text></svg>
        <div class="card-body">
          <h5 class="card-title">Balloonとは</h5>
          <p class="card-text">インターネット上の誰かと会話するサービスです。</p>
          <router-link to="/balloonpage" class="btn btn-primary mx-2">
            はじめる
          </router-link>
        </div>
      </div>

      <div class="card" style="width: 54rem;">
        <svg class="bd-placeholder-img card-img-top" width="300%" height="180" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Image cap"><title>Placeholder</title><rect fill="#868e96" width="100%" height="100%"/><text fill="#dee2e6" dy=".3em" x="50%" y="50%">Image cap</text></svg>
        <div class="card-body">
          <h5 class="card-title">Balloonとは</h5>
          <p class="card-text">インターネット上の誰かと会話するサービスです。</p>
          <router-link to="/balloonpage" class="btn btn-primary mx-2">
            はじめる
          </router-link>
        </div>
      </div>

      <div class="card" style="width: 54rem;">
        <svg class="bd-placeholder-img card-img-top" width="300%" height="180" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Image cap"><title>Placeholder</title><rect fill="#868e96" width="100%" height="100%"/><text fill="#dee2e6" dy=".3em" x="50%" y="50%">Image cap</text></svg>
        <div class="card-body">
          <h5 class="card-title">Balloonとは</h5>
          <p class="card-text">インターネット上の誰かと会話するサービスです。</p>
          <router-link to="/balloonpage" class="btn btn-primary mx-2">
            はじめる
          </router-link>
        </div>
      </div>

    </div>
    



  </div>
</template>


<script>
import axios from 'axios'
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
  methods: {
    getAPI () {
      // this.result = "this is test"
      axios.get(this.url)
      .then(response => {
        this.result = response.data.message
      })
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
