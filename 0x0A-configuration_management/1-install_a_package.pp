# puppet script to install flask from pip3

package {'python':
  ensure   => '3.8.10',
}
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
package {'Werkzeug':
  ensure   => '2.1.1',
}
