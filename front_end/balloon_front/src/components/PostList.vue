<template>
  <div>
    <div v-for="(post, key) in rand_posts" :key="key">
    <!-- <div v-for="post in rand_posts" :key="post.id"> -->
      <hr>
      <!-- <p>カテゴリ: {{ post.category.name }}</p> -->
  
      <p>{{ post.author }}</p>
      
      
      <p>{{ post.content }}</p>
      <!-- <p>{{ post.image }}</p> -->
      <p>日付: {{ moment(post.published_at) }}</p>
      <hr>
    </div>
    <p>this is test</p>
  </div>
</template>


<script>
import axios from 'axios'
import moment from 'moment'

moment.locale("ja")

export default {
    name: 'PostList',
    data() {
        return {
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
        }
    }
};
</script>