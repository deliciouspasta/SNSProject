<template>
  <div class="alert alert-primary">
    <!-- <img alt="balloon back" src="../assets/balloon_back.png"> -->
    <h2>{{title}}</h2>
    <p>{{message}}</p>
    <button class="btn btn-primary m-3"
      v-on:click="doAction">
    {{btn}}
    </button>
    <transition name="transit">
      <p v-if="flg" class="alert alert-light h5">
        Transition context!
      </p>
    </transition>




    <div class="card-deck">
      
      <div class="card" style="width: 54rem;">
        <svg class="bd-placeholder-img card-img-top" width="300%" height="90" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Image cap"><title>Placeholder</title><rect fill="#868e96" width="100%" height="100%"/><text fill="#dee2e6" dy=".3em" x="50%" y="50%">Image cap</text></svg>
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
export default {
  name: 'Balloon',

  data() {
    return {
      title: 'Trans&Anim',
      message:'This is Transition sample!',
      flg:true,
      btn:'Show/Hide',
    }
  },
  methods:{
    doAction(){
      this.flg = !this.flg
    },
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
.trans {
  background-color:black;
  color: white;
  padding:10px;
  font-size:20pt;
}
.transit-enter-active {
  transition: opacity 3.5s;
  animation: anim 3.5s reverse;
}
.transit-leave-active {
  transition: opacity 5.0s;
  animation: anim 5.0s;
}
.transit-enter-from {
 opacity: 0;
}
.transit-enter-to {
 opacity: 1.0;
}

@keyframes anim {
  0% {
    transform: translateX(0px) translateY(0px);
    opacity:1.0;
    background-color: #ddf;
  }
  25% {
    transform: translateX(250px) translateY(0px);
    opacity:1.0;
    background-color: #fdd;
  }
  50% {
    transform: translateX(0px) translateY(-100px);
    opacity:1.0;
    background-color: #dfd;
    }
  75% {
    transform: translateX(250px) translateY(-100px);
    opacity:1.0;
    background-color: #fdf;
  }
  100% {
    transform: translateX(0px) translateY(-200px);
    opacity:0;
    background-color: #ffd;
  }
}

</style>
