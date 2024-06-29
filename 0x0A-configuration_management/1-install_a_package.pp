# puppet script to install flask from pip3

package {'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
package {'Python':
  ensure   => '3.8.10',
}
package {'Werkzeug':
  ensure   => '2.1.1',
}
