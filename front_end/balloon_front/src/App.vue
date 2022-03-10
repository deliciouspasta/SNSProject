<template>
  <div id="nav">
    
    <HelloWorld/>
    <router-view/>
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>

    <router-link to="/" class="btn btn-primary mx-2">
        Go to Top
    </router-link>
    <router-link to="/balloonpage" class="btn btn-warning">
        Go to Balloon
    </router-link>

    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <router-view></router-view> -->
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data(){
    return{
      title: 'Router'
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  background-color: #e2fff6;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
