<template>
    <div>
        <!-- <div><p>{{ msg }}</p></div> -->
        <div class="h2">
            <p>Encuenta sobre uso de Redes Sociales</p>
        </div>
        
        <div>
            <form id="">
                <div class="row">
                    <label class="col-form-label">Nombre </label>
                    <input type="text" class="form-control form-control-sm" >
                </div>
                <div>
                    <label class="col-form-label">Email </label>
                    <input type="email" class="form-control form-control-sm">
                </div>
                <div>
                    <label class="col-form-label">Edad </label>
                    <select class="form-select form-select-sm" >
                        <option selected>Seleccione rango de edad</option>
                        <option value="">18-25 years</option>
                        <option value="">26-33 years</option>
                        <option value="">34-40 years</option>
                        <option value="">40+ years</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label ">Tiempo promedio al dia en Tiktok al dia </label>
                    <select class="form-select form-select-sm" >
                        <option selected>Seleccione su tiempo en horas</option>
                        <option value="0">0</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label">Tiempo promedio al dia en WhatsApp al dia </label>
                    <select class="form-select form-select-sm" >
                        <option selected>Seleccione su tiempo en horas</option>
                        <option value="0">0</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label">Tiempo promedio al dia en Twitter al dia </label>
                    <select class="form-select form-select-sm" >
                        <option selected>Seleccione su tiempo en horas</option>
                        <option value="0">0</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label">Tiempo promedio al dia en Instagram al dia </label>
                    <select class="form-select form-select-sm" >
                        <option selected>Seleccione su tiempo en horas</option>
                        <option value="0">0</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label ">Tiempo promedio al dia en Facebook al dia </label>
                    <select class="form-select form-select-sm" >
                        <option selected>Seleccione su tiempo en horas</option>
                        <option value="0">0</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>
                <div class="col-12 form-group text-center">
                    <button class="btn vue-bg btn-lg col-4">Cargar</button>
                </div>
                </div>
            </form>
        </div>
        

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style>
.vue-bg{
    background-color: rgba(111, 207, 224, 0.705);
}
</style>

