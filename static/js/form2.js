window.addEventListener("DOMContentLoaded", () => {

    document.querySelector('.send').addEventListener('click', () => {
        let data = document.querySelectorAll('.rad input');
        let result = []
        let user = document.getElementById('user_id').value;
        for (let i = 0; i < data.length; i++) {
            if (data[i].checked) {
                result[result.length ] = {
                    question: data[i].id,
                    value: data[i].value,
                    user: user
                }
            }

        }
        console.log(result)
        // осталось запушить на отдельный роут этот result
        fetch(`http://127.0.0.1:8000/education/data/${JSON.stringify(result)}/`)
    })


})