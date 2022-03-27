<template>
  <div id="nav">
  <v-app id="inspire">
      <v-navigation-drawer
        color="#ffeae6"
        v-model="drawer"
        app
      >
        <v-list rounded>
          <v-subheader>ナビゲーション</v-subheader>
          <v-list-item-group
            v-model="selectedItem"
            color="primary"
          >
            <v-list-item
              
              v-for="(item,key) in items"
              :key="key"
              :to="item.link"
            >
              <v-list-item-content
                
              >
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>

      <v-app-bar app
        dark
        color="error"
      >
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title
          class="white--text font-weight-bold"
        >Balloon</v-toolbar-title>

        <v-row class="justify-end">
          <v-btn
            class="white--text"
            rounded
            color="error"
            
            to="/auth"
            >
            Sign in
          </v-btn>
        </v-row>

        
      </v-app-bar>

      <v-main>
          <HelloWorld/>
          <router-view/>
      </v-main>

    <v-footer padless>
        <v-col
          class="error text-center"
          cols="12"
          no-gutters
          fluid
        >
          {{ new Date().getFullYear() }} — <strong>Balloon</strong>
        </v-col>
      </v-footer>

  </v-app>

      

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
      title: 'Router',
      drawer: null,

      selectedItem: 1,
      items: [
        { text: 'Home', link:'/'},
        { text: '投稿一覧', link:'/postlist'},
        { text: '投稿ページ', link:'/postpage'},
      ],
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
  height: 100vh;
  background-color: #f8fffd;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
