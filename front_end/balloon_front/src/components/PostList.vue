<template>
    <v-container class="grey lighten-5">
        <p></p>
        <h2>※投稿が反映されない場合は、再読み込みをしてください</h2>
        <p></p>
      <div class="text-center">

      <v-row>

        <v-col>

          <v-btn
            class="white--text md-6"
            rounded
            color="primary"
            block
            to="/postpage"
            
          >
            投稿ページへ
          </v-btn>
          </v-col>
      </v-row>
    </div>

      <v-row dense
      >
        <v-col
          v-for="(post, key) in rand_posts" :key="key"
        >
            <v-card
                class="mx-auto"
                max-width="344"
                elevation="10"
            >
            <v-img
                :src="imgSrc(post)"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="200px"
                class="white--text align-end font-weight-bold"
            >
            <v-card-title v-text="post.author"></v-card-title>
            </v-img>

            <v-card-title>
              <p class="font-weight-bold">{{ post.content }}</p>
            </v-card-title>


            <v-card-actions>

            <v-btn
                icon
                @click="show = !show"
            >
                <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
            </v-btn>
            </v-card-actions>

            <v-expand-transition>
            <div v-show="show">
                <v-divider></v-divider>

                <v-card-text>
                    <p>日付: {{ moment(post.published_at) }}</p>
                </v-card-text>
            </div>
            </v-expand-transition>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>


<script>
import axios from 'axios'
import moment from 'moment'

moment.locale("ja")

export default {
    name: 'PostList',
    data() {
        return {
            show: false,
            Posts: [],
            rand_posts:[]
        };
    },
    mounted() {
        axios
            .get("http://localhost:8000/back_end/balloon/posts/")
            .then(response =>{
                this.Posts = response.data
                this.rand_posts = this.shuffle(this.Posts)
            })
            .catch(error => console.log(error))
    },

    computed: {
        imgSrc: function(){
            return function(post){
                return post.image
            }
            
        }
    },

    methods:{
        moment: function(date){
            return moment(date).format('YYYY/MM/DD HH:mm:SS')
        },
        shuffle: function(rand_posts){
            for (var i = rand_posts.length -1; i > 0; i--){
                var j = Math.floor(Math.random() * (i + 1))
                if (i == j) continue
                var k = rand_posts[i]
                rand_posts[i] = rand_posts[j]
                rand_posts[j] = k
            }
            return rand_posts
        },
    }
};
</script>