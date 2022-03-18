<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >


    <v-text-field
      v-model="credentials.username"
      :counter="100"
      maxlength="100"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <v-text-field
      type="password"
      v-model="credentials.password"
      :counter="30"
      maxlength="30"
      :rules="passwordRules"
      label="Password"
      required
    ></v-text-field>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="login"
    >
      LOGIN
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset Form
    </v-btn>

  </v-form>
</template>

<script>
import axios from 'axios'
import router from '../../router'

  export default {
    data: () => ({
      valid: true,
      loading:false,
      credentials: {},
      emailRules: [
        // v => !!v || 'メールアドレスを入力してください',
        // v => /.+@.+\..+/.test(v) || 'メールアドレスを入力してください',
      ],
      passwordRules:[
        v => !!v || "パスワードを入力してください",
        v => (v && v.length > 8) || "パスワードは８文字以上です",
      ],
      select: null,
    }),
    methods: {
      login(){
          if (this.$refs.form.validate()) {
            this.loading = true;
            axios.post('http://localhost:8000/back_end/balloon/auth/', this.credentials).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                router.push('/balloonpage');
            })
          }
      },
      reset () {
        this.$refs.form.reset()
      },
    },
  }
</script>