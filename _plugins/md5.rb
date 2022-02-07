require 'digest'

module MD5Filter
  def md5 (input)
    md5 = Digest::MD5.new
    md5.update input
    md5.hexdigest
  end
end

Liquid::Template.register_filter(MD5Filter) # register filter globally
