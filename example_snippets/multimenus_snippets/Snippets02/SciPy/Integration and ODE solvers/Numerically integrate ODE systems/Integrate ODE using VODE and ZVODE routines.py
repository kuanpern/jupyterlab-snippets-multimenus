def f(t, y, arg1):
    return [1j*arg1*y[0] + y[1], -arg1*y[1]**2]
def jac(t, y, arg1):
    return [[1j*arg1, 1], [0, -arg1*2*y[1]]]
y0 = [1.0j, 2.0]
t0, t1, dt = 0.0, 10.0, 1.0
r = integrate.ode(f, jac).set_integrator('zvode', method='bdf')
r.set_initial_value(y0, t0)
r.set_f_params(2.0)
r.set_jac_params(2.0)
while r.successful() and r.t < t1:
    r.integrate(r.t+dt)
    print('{0}: {1}'.format(r.t, r.y))