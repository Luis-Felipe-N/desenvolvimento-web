// const btnOpenDropdownUser = document.querySelector('[data="btnOpenDropdownUser"]')
const btnOpenDropdownUser = document.getElementById("btn-open-dropdown-user")
const dropdownUser  = document.querySelector('[data="dropdownUser"]')

const handleOpenDropdownUser = (event) => {
    dropdownUser.classList.toggle('active')
}

console.log(btnOpenDropdownUser, dropdownUser)

btnOpenDropdownUser.addEventListener('click', handleOpenDropdownUser)