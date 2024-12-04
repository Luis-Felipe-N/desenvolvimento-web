import clickOutSide from "./modules/clickoutside.js"

const inputImagem = document.querySelector('[data="inputImage"]')
const imageName = document.querySelector('[data="imageName"]')

const handleNameFile = (event) => {
    const nameImage = event.target.files[0].name
    const nameFormated = `${nameImage.slice(0, 10)}...`

    imageName.textContent = nameImage
}

const btnOpenModalPreviewImage = document.querySelector('[data="btnOpenImagePreview"]')
const btnCloseModalPreviewImage = document.querySelector('[data="btnCloseImagePreview"]')
const modalModalPreviewImage = document.querySelector('[data="modalPreviewImage"]')


const handleCloseModal = (event) => {
    event.preventDefault()
    modalModalPreviewImage.classList.remove('active') 

    btnCloseModalPreviewImage.removeEventListener('click', handleCloseModal)
}

const handleOpenModalPreviewImage = (event) => {
    event.preventDefault()
    modalModalPreviewImage.classList.add('active')

    btnCloseModalPreviewImage.addEventListener('click', handleCloseModal)
}

inputImagem.addEventListener('change', handleNameFile)

btnOpenModalPreviewImage.addEventListener('click', handleOpenModalPreviewImage)