import { Link, useMatch, useResolvedPath } from "react-router-dom"

export default function Navbar() {
  return (
    <nav className="nav">
      <h1><CustomLink to="/Home">Home</CustomLink></h1>  
       <h1> <CustomLink to="/about">About</CustomLink></h1>
       <h1> <CustomLink to="/contact">Contact</CustomLink></h1>
       </nav>
  )
}

function CustomLink({ to, children, ...props }) {
const resolvedPath = useResolvedPath(to)
const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <ul>
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
    </ul>
  )
}
