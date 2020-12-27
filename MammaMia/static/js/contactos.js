var app = new Vue({
    el: "#app",
    data : {
        lista : [
           
        ],
        nombre : '',
        email : '',
        num: ''
    },
    methods: {
        addContacto: function(){
            if(this.nombre != "" && this.email != "" && this.num != ""){
                this.lista.push({nombre:this.nombre, email: this.email, num: this.num});
                this.nombre = "";
                this.email = "";
                this.num ="";
            }
            else{
                alert("Debe rellenar todos los campos");
            }
        },
        eliminarContacto: function(index){
            if(confirm("Seguro que quieres borrar este contacto?")){
                this.lista.splice(index,1);
            }
        }
    },
})
