// let test = document.getElementById('test')
// test.addEventListener("click", function(){
//     console.log(test);
//     test.style.background = "blue"
// })

let gameForm = document.getElementById('createGame')
gameForm.addEventListener('submit', function(event){
    event.preventDefault()
    
    let gameFormData = new FormData(gameForm)

    fetch('http://localhost:5000/game/create', {method:'POST', body:gameFormData})
    .then(resp => console.log(resp))
    .catch(err => console.log(err))

})

document.querySelectorAll('.likeBtn').forEach(item => {
    item.addEventListener('click', function(e){
        e.preventDefault()
        // game/{{game.id}}/like
        let game = this
        game_id = game.getAttribute('game_id');

        fetch(`/game/${game_id}/like`)
        .then(resp => function(){
            // game.
        })
        .catch(err => console.log(err))
    })
})