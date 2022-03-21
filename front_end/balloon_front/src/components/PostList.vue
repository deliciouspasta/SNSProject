<template>
  <div>
    <div v-for="(post, key) in Posts" :key="key">
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
            Posts: []
        };
    },
    mounted() {
        axios
            .get("http://localhost:8000/back_end/balloon/posts/")
            .then(response => (this.Posts = response.data))
            .catch(error => console.log(error))
    },
    methods:{
        moment: function(date){
            return moment(date).format('YYYY/MM/DD HH:mm:SS')
        }
    }
};
</script>