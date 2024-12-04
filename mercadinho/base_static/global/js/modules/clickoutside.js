function clickOutSide(elements) {
    document.addEventListener('click', handleClick)

    function handleClick(event){
        elements.forEach((element) => {
            
            if (element.contains(event.target)) {
                element.classList.remove('active')
                document.removeEventListener('click', handleClick)
            }


        })

        console.log(elements)

    }

}

export default clickOutSide 