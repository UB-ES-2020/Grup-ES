<template>
  <div id="app">
  <div>
    <navbar ref="c" @changeShowState="show = !show"/>

    <b-container v-if= "show === true">
      <div class="row d-flex justify-content-center">
      <b-col sm="3" md="6" lg="6" xl="4">
      <div class="form-control  bg-light" style="margin-top: 150px">
      <div class="form-label-group">
              <b-button variant="link" style="margin-left: 100px" @click="goRegister()">¿Quieres crear una cuenta?</b-button>
              <br>
              <br>
              <h5>Iniciar Sesión</h5>
              <input type="email" id="inputEmail" class="form-control"
              placeholder="Correo electrónico" required autofocus v-model="email" style="margin-top: 15px">
              <input type="password" id="inputPassword" class="form-control"
              placeholder="Password" required v-model="password" style="margin-top: 20px">
              <b-form-text style="margin-top: 15px; margin-left: 5px">
                Al continuar confirmas que aceptas las <a>Condiciones de uso</a> y las <a>Políticas de privacidad</a>
              </b-form-text>
              <b-button block variant="danger" style="margin-top: 20px" @click="checkLogin()">Log In</b-button>
              <b-button block variant="link" style="margin-top: 10px" @click="changePassword()">¿Olvidaste contraseña?</b-button>
      </div>
      </div>
      </b-col>
      </div>
    </b-container>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import navbar from './subcomponents/navbar'

export default {
  components: {
    navbar
  },
  data: () => ({
    show: true,
    id: '',
    username: '',
    email: '',
    password: '',
    role: '',
    token: '',
    userObject: {username: '', email: '', role: '', token: ''}
  }),
  methods: {
    checkLogin () {
      const parameters = {
        email: this.email,
        password: this.password
      }
      const path = this.$API_URL + 'login'
      const path2 = this.$API_URL + 'user/' + this.email
      axios.all([
        axios.post(path, parameters),
        axios.get(path2)
      ])
        .then(axios.spread((datapost, dataget) => {
          this.token = datapost.data.token
          this.id = dataget.data.user.id
          this.username = dataget.data.user.username
          this.email = dataget.data.user.email
          this.role = dataget.data.user.role
          this.createUserObject(this.id, this.username, this.email, this.role, this.token)
          this.$refs.c.showToast(['Info', 'Log in realizado con exito'])
          setTimeout(() => window.location.replace('/'), 3000)
          this.initForm()
        }))
        .catch((error) => {
          console.error(error)
          this.initForm()
          this.$refs.c.showToast(['Error', 'Correo o contraseña incorrectas'])
        })
    },
    createUserObject (id, username, email, role, token) {
      this.userObject.id = id
      this.userObject.username = username
      this.userObject.email = email
      this.userObject.role = role
      this.userObject.token = token
      localStorage.setItem('user_session', JSON.stringify(this.userObject))
      console.log(this.userObject.id, this.userObject.username, this.userObject.email, this.userObject.role, this.userObject.token)
    },
    goRegister () {
      this.$router.push({path: '/userregister'})
    },
    initForm () {
      this.email = ''
      this.password = ''
    },
    changePassword () {
      this.$router.push({path: '/change'})
    }
  }
}
</script>
