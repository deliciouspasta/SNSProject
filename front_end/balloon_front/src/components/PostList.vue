<template>
    <v-container class="grey lighten-5">
      <v-row
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
                src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                height="200px"
            ></v-img>

    

            <v-card-title>
            <p>---------</p>
            <p>{{ post.author }}</p>
            <p>---------</p>
            
            <p>{{ post.content }}</p>
            <!-- <p>日付: {{ moment(post.published_at) }}</p> -->
            </v-card-title>


            <v-card-actions>
            <v-btn
                color="orange lighten-2"
                text
                @click="reply"
            >
                返信する
            </v-btn>

            <v-spacer></v-spacer>

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
        reply(){
            
        },
    }
};
</script>