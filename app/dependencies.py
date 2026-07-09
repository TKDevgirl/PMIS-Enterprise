from fastapi import Header, HTTPException


def require_admin(x_role: str = Header(default="viewer", alias="X-Role")):
    if x_role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Viewer is read-only. Use X-Role: admin.")
    return x_role
